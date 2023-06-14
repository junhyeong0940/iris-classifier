프로젝트 설명 및 소감

이 프로젝트에서 @dataclass 정의를 이용해 디자인을 살펴 보았다.

@dataclass
class Sample:

    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    
이 코드에서 @dataclass 데코레이터를 사용해 제공된 속성 타입 힌트로부터 클래스를 생성했다.


@dataclass
class KnownSample(Sample):
    species: str



@dataclass
class TestingKnownSample(KnownSample):
    classification: Optional[str] = None


@dataclass

class TrainingKnownSample(KnownSample):
    pass


이 코드는 @dataclass 데코레이터로 정의딘 클래스의 인스턴스를 생성하는 방법을 보여준다.

@dataclass

class Hyperparameter:

    k: int
    algorithm: Distance
    data: weakref.ReferenceType["TrainingData"]

    def classify(self, sample: Sample) -> str:
    
        if not (training_data := self.data()):
            raise RuntimeError("No TrainingData object")
        distances: list[tuple[float, TrainingKnownSample]] = sorted(
            (self.algorithm.distance(sample, known), known)
            for known in training_data.training
        )
        k_nearest = (known.species for d, known in distances[: self.k])
        frequency: Counter[str] = collections.Counter(k_nearest)
        best_fit, *others = frequency.most_common()
        species, votes = best_fit
        return species
이 코드는 from__future__import annotations를 사용시에 재밌는 기능을 보여주는데 weakref.ReferenceType["TrainingData"]의 값은 두 가지 뚜렷한 목표를 갖는데 weakref.ReferenceType["TrainingData"]를 제공해야하고 클래스 정의를 빌드하기 위해 @dataclass 데코레이터에 의해 런타임에 평가될  추가적인 타입 한정자는 사용되지 않는다.

 마지막으로 이 수업을 들으면서 소감은 솔직하게 수업이 정말정말 어려웠었다. 수업내용을 따라가지 못해 너무 힘들곤했었는데 공부를 하나 하나 해보면서 객체 지향 프로그래밍은 정말 중요하고 우리가 사용하는 컴퓨터 언어에도 객체지향 언어가 많이 쓰이고 있다는 것을 알게 되었다. 한 학기동안 파이썬으로 아이리스 꽃종 분류 개발 아키텍처를 하면서 힘들고 어려웠지만 코딩으로 내가 설계했던 부분을 생각해보면 그래도 나음 재밌었고, 나에게 정말 가치 있었던 수업이었던것 같다. 교수님 한 학기동안 고생많으셨습니다. 감사합니다!!
