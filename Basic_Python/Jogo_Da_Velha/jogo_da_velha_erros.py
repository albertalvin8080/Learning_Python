class JogadorInvalidoError(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)

class PosicaoOcupadaError(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)
