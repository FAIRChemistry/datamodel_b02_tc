from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .componentinformation import ComponentInformation


@forge_signature
class SyringePump(ComponentInformation):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("syringepumpINDEX"),
        xml="@id",
    )

    placeholder: Optional[int] = Field(description="placeholder", default=None)

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="4c9b99d8f8bfef1da92cd9da2ca6cc7487cee9fe"
    )
