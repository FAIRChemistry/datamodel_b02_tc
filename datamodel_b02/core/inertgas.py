from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .chemical import Chemical


@forge_signature
class InertGas(Chemical):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("inertgasINDEX"),
        xml="@id",
    )

    placeholder: Optional[int] = Field(description="placeholder", default=None)

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="1e3c1dd9ffd79c2ed7f59e418212f341e9c2f977"
    )
