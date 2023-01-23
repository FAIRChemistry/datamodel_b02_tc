import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Insulation(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("insulationINDEX"),
        xml="@id",
    )

    insulation_material: Optional[str] = Field(
        description="material of which the insulation is made of.", default=None
    )

    thickness: Optional[float] = Field(
        description="thickness of the insulation in mm.", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02_tc.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="41a609850676450d6df0f1c036836a32e74f1eaf"
    )
