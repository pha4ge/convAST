#!/usr/bin/env python
import dataclasses


@dataclasses.dataclass
class ConvAST:
    """
    Single INSDC compatible AST result entry
    Should be generated directly from LinkML yaml
    """

    def to_ena(self):
        """
        Export just ENA fields
        """
        raise NotImplementedError("ENA export not implemented")

    def to_ncbi(self):
        """
        Export just NCBI fields
        """
        raise NotImplementedError("NCBI export not implemented")
