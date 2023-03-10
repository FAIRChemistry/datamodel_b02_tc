import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .flowmodule import FlowModule
from .measuringinstrument import MeasuringInstrument
from .reactor import Reactor


@forge_signature
class Device(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("deviceINDEX"),
        xml="@id",
    )

    measuring_instruments: Optional[MeasuringInstrument] = Field(
        description="instrument that measures a physical quantity.", default=None
    )

    reactors: Optional[Reactor] = Field(
        description="tubing or vessel in which the reaction takes place.", default=None
    )

    flow_modules: Optional[FlowModule] = Field(
        description="component involved in the transport of media.", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02_tc.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="c797b854fa0b6a85438601dcbd3056189258ba98"
    )
