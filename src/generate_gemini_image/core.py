import logging
from pathlib import Path
from typing import List, Optional

import vertexai
from vertexai.preview.vision_models import ImageGenerationModel

from .utils import ensure_directory, sanitize_filename

logger = logging.getLogger(__name__)


class ImageGenerator:
    def __init__(self, project_id: str, location: str, model_name: str):
        self.project_id = project_id
        self.location = location
        self.model_name = model_name
        self._model = None
        self._init_vertex()

    def _init_vertex(self):
        vertexai.init(project=self.project_id, location=self.location)

    @property
    def model(self):
        if not self._model:
            try:
                self._model = ImageGenerationModel.from_pretrained(self.model_name)
            except Exception as e:
                logger.error(
                    f"Failed to load ImageGenerationModel '{self.model_name}': {e}"
                )
                raise
        return self._model

    def generate(
        self,
        prompt: str,
        count: int = 1,
        aspect_ratio: str = "1:1",
        negative_prompt: Optional[str] = None,
        person_generation: str = "allow_all",
        safety_filter_level: str = "block_some",
        add_watermark: bool = True,
        seed: Optional[int] = None,
        guidance_scale: int = 9,
        output_dir: Path = Path("."),
    ) -> List[Path]:

        logger.info(f"Generating {count} image(s) with prompt: '{prompt}'")

        # Ensure output directory exists
        ensure_directory(output_dir)

        try:
            response = self.model.generate_images(
                prompt=prompt,
                number_of_images=count,
                aspect_ratio=aspect_ratio,
                negative_prompt=negative_prompt,
                person_generation=person_generation,
                safety_filter_level=safety_filter_level,
                add_watermark=add_watermark,
                seed=seed,
                guidance_scale=guidance_scale,
            )
        except Exception as e:
            logger.error(f"Image generation failed: {e}")
            raise

        saved_files = []
        for i, image in enumerate(response):
            filename = sanitize_filename(prompt)
            # handle collision or multiples
            if count > 1:
                name_stem = Path(filename).stem
                suffix = Path(filename).suffix
                filename = f"{name_stem}_{i}{suffix}"

            output_path = output_dir / filename
            image.save(location=str(output_path), include_generation_parameters=True)
            saved_files.append(output_path)
            logger.info(f"Saved: {output_path}")

        return saved_files
