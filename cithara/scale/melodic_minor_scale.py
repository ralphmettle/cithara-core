from cithara.note import Note
from cithara.scale.base import Scale, ScaleBuilder, SCALE_FORMULA


class MelodicMinorScale(Scale):
    def __init__(self, root: Note) -> None:
        super().__init__(root=root, type="melodic_minor")
