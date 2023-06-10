import math
import datetime
from typing import Optional, Iterable, Union, Counter


class Sample:
    """Abstract superclass for all sample classes"""
    def __init__(
        self,
        sepal_length: float,
        sepal_width: float,
        petal_length: float,
        petal_width: float,
        species: Optional[str] = None
    ) -> None: #리턴할게 아무것도 없다.
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width                    #인공지능에 까지 4가지를 넣으면, 예측해서 다븡ㄹ 낼거임// 그거 저장을 클래시피케이션에
        self.species = species
        self.classification: Optional[str] = None # self 안에서 정의 안되어서 밖에서는 사용 불가능

    def __repr__(self) -> str:
        if self.species is None:
            known_unknown = "UnknownSample"
        else:
            known_unknown = "KnownSample"
        if self.classification is None:
            classification = ""
        else:
            classification = f", classification={self.classification}"
        return (
            f"{known_unknown}("
            f"sepal_length={self.sepal_length},"
            f"sepal_width={self.sepal_width},"
            f"petal_length={self.petal_length},"
            f"petal_width={self.petal_width},"
            f"species={self.species!r}"
            f"{classification}"
            f")"
        )
    
    def classify(self, classification: str) -> None:
        self.classification = classification

    def matches(self) -> bool:
        return self.species == self.classification

class knownSample(sample):
     def __init__(
        self,
        species: str,
        sepal_length: float,
        sepal_width: float,
        petal_length: float,
        petal_width: float,     
    ) -> None:
         super().__init__(
             sepal_length = sepal_width,
             sepal_width=sepal_width,
             petal_length = petal_length,
             petal_width = petal_width
         )
         self.species = species

    def ___reper__(self) -> str: 
        return (
            f"{self.__class__.__name__}("
            f"sepal_length={self.sepal_length},"
            f"sepal_width={self.sepal_width},"
            f"petal_length={self.petal_length},"
            f"petal_width={self.petal_width},"
            f")"
        )
    
    


class Unknownsample(Sample):
    """Sample provided by an user, not yet classified."""
    pass

class TrainingknownSample:
    pass

class TestingknownSample(knownSample):
    def __init__(
            self,
            species: str,
            sepal_length: float,
            sepal_width: float,
            petal_length: float,
            petal_width: float,
            classification: Optional[str] = None
    )-> None:
        super().__init__(
            species = species,
            sepal_length = sepal_width,
            sepal_width=sepal_width,
            petal_length = petal_length,
            petal_width = petal_width
        )     
        self.classification = classification

    def __reper__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"sepal_length={self.sepal_length},"
            f"sepal_width={self.sepal_width},"
            f"petal_length={self.petal_length},"
            f"petal_width={self.petal_width},"
            f"species={self.species!r},"
            f"classification{self.classification!r}"
            f")"
        )
    
    
    def matches(self) -> bool:
        return self.species == self.classification

class ClassifiedSample:(Sample):
def __init__(self, classification, sample) -> None:
        super().__init__(
            sepal_length= sepal_length,
            sepal_width= sepal_width,
            petal_length=sample.petal_legnth,
            petal_width=sample.petal_width
        )
        self.classification = classification

    def __reper__(self) -> str:
       return (
               f"{self.__class__.__name__}("
            f"sepal_length={self.sepal_length},"
            f"sepal_width={self.sepal_width},"
            f"petal_length={self.petal_length},"
            f"petal_width={self.petal_width},"
            f"species={self.species!r},"
            f"classification{self.classification!r}"
            f")"
       )


class TrainingData:
    def __init__(self) -> None:
        pass                       # 먼저 선언되어야 하나?


class Distance:
    def distance(self, s1: Sample, s2: Sample) -> float:
        pass

class ED(Distance):
    def distance(self, s1: Sample, s2: Sample) -> float:
        return math.hypot(
            s1.sepal_length - s2.sepal_length,
            s1.sepal_width - s2.sepal_width,
            s1.petal_length - s2.petal_length,
            s1.petal_width - s2. petal_width
        )

class MD(Distance):
    def distance(self, s1: Sample, s2: Sample) -> float:
        return sum([
            abs(s1.sepal_length - s2.sepal_length),
            abs(s1.sepal_width - s2.sepal_width),
            abs(s1.petal_length - s2.petal_length),
            abs(s1.petal_width - s2. petal_width)
        ])
class CD:
    """TODO""" 
    pass

class SD:
    pass

class Hyperparameter:
    def __init__(self, k: int,algorithm: Distance, training: "TrainingData") -> None:
        self.k = k
        self. algorithm = algorithm
        self.data = training
        self.quality: float

    def classify(self, sample: Union[Unknownsample, TestingknownSample]) -> str:
        """TOOD: K-NN 알고리즘"""
        training_data = self.data
        if not training_data:
            raise RuntimeError("No TrainingData object!")
        distances: list[tuple[float, TrainingknownSample]] = \
            sorted(
                (self.algorithm. distance(sample, known), known)
                for known in training_data.training
            )
        k_nearest: tuple[str] = (known.species for d, known in distances[:self.k])
        frequency: Counter[str] = collections.Counter(k_nearest)
        best_fit, *others = frequency.most_common() 
        species, votes = best_fit
        return species 
    
    def test(self) -> None:
        training_data: Optional["TrainingData"] = self.data
        if not training_data:
            raise RuntimeError("")
        pass_count, fail_count = 0, 0
        for sample in self.training_data.testing:
            sample.classification = self.classify(sample)
            if sample.matches():
                pass_count += 1
            else:
                fail_count += 1
        self.quality = pass_count / (pass_count + fail_count)


class TrainingData:
    def __init__(self, name: str) -> None:
        self.name = name
        self.uploaded: datetime.datetime
        self.tested: datetime.datetime
        self.training: list[Sample] = []
        self.testing: list[Sample] = []
        self.tuning: list[Hyperparameter] = []

    def load(self, raw_data_source: Iterable[dict[str, str]]) -> None:
        for n, row in enumerate(raw_data_source):
            sample = Sample(
                sepal_length=float(row["sepal_length"]),
                sepal_width=float(row["sepal_width"]),
                petal_length=float(row["petal_length"]),
                petal_width=float(row["petal_width"]),
                species=row["species"]
            )
        if n % 5 == 0:
            self.testing.append(sample)
        else:
            self.training.append(sample)
    self.uploaded = datetime.datetime.now(tz=datetime.timezone.utc)

    def test(self, parameter: Hyperparameter) -> None:
        parameter.test()
        self.tuning.append(parameter)
        self.tested = datetime.datetime.now(tz=datetime.timezone.utc)

    def classify(self, parameter: Hyperparameter, sample: Sample):
        classification = parameter.classify(sample)
        sample.classify(classification)
        return sample



if __name__ == "__main__":
    sample = Sample(2.0, 2.0, 20.2, 30.1, "Virginica")
    print(sample.classify("Sentosa"))
    print(sample.matches())

