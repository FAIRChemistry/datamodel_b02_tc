import sdRDM

from typing import Optional, Union
from typing import List
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .stoichiometry import Stoichiometry


@forge_signature
class Chemical(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("chemicalINDEX"),
        xml="@id",
    )

    name: List[str] = Field(
        description="IUPAC name of the compound.", default_factory=ListPlus
    )

    formula: Optional[str] = Field(
        description="molecular formula of the compound.", default=None
    )

    pureness: Optional[float] = Field(
        description="pureness of the compound in percent.", default=None
    )

    supplier: Optional[str] = Field(
        description="name of the supplier of the compound.", default=None
    )

    stoichiometry: Optional[Stoichiometry] = Field(
        description=(
            "stoichiometric information like equivalents, mass, amount of substance,"
            " volume"
        ),
        default=None,
    )

    state_of_matter: Optional[str] = Field(
        description="s for solid, l for liquid and g for gaseous", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/datamodel_b02_tc.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="c797b854fa0b6a85438601dcbd3056189258ba98"
    )
