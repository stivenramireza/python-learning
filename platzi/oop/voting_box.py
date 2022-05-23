class VotingBox:
    def __init__(self, identifier: int, regions: list[str]) -> None:
        self._identifier = identifier
        self._regions = regions
        self._region = None

    @property
    def region(self) -> str:
        return self._region

    @region.setter
    def region(self, region: str) -> None:
        if region not in self._regions:
            raise ValueError(f'The region {region} is not valid')
        self._region = region


def main() -> None:
    voting_box = VotingBox(123, ['Ciudad de México', 'Morelos'])
    print(voting_box.region)
    voting_box.region = 'Ciudad de México'
    print(voting_box.region)


if __name__ == '__main__':
    main()
