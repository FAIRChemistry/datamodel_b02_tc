from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .componentinformation import ComponentInformation


@forge_signature
class MassFlowController(ComponentInformation):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("massflowcontrollerINDEX"),
        xml="@id",
    )

    minimum_mass_flow: Optional[float] = Field(
        description="minimum volume flow in SCCM.", default=None
    )

    maximum_mass_flow: Optional[float] = Field(
        description="maximum volume flow in SCCM.", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="77e70dd05752c75381f94d10c2488f1e8d2ddd01"
    )
