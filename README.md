# E-nose Data Analysis [![Tests](https://github.com/aungkhantmaw64/enose-data-analysis/actions/workflows/tests.yml/badge.svg)](https://github.com/aungkhantmaw64/enose-data-analysis/actions)
## Introduction
This repository contains analytics for the experimental ordor dataset I created using the hybrid-electronic nose designed as an aiding device for non-invasive diaganosis. I published an IEEE research article as a main author based on this device and the code used for the analytics of the dataset can be found in this repo. For the published article, please refer to https:/ieeexplore.ieee.org/document/9495905.

## Architectural Diagram

### Sensor Responses
```mermaid
classDiagram
    MetalOxideSensorResponse --> "1..*" Transient: Contains
    Transient <|.. Voltage: Implements
    Transient <|.. Current: Implements
    Transient <|.. Conductance: Implements

    class MetalOxideSensorResponse{
        -transients: Dict~str, Transient~
        -duration_s: Integer
        +addTransient(id: str, transient: Transient) void
        +removeTransient(id: str) void
        +getTransients(void) Dict~str, Dataframe~
    }
    class Transient{
        <<Interface>>
        + get() DataFrame
    }
    class Voltage{
        -csvPath: str
    }
    class Current{
        -csvPath: str
    }
    class Conductance{
        -csvPath: str
    }
```

### Sample Reading
```mermaid
classDiagram
    SampleReader *-- SamplePathChecker: Has
    SamplePathChecker <.. DefaultPathChecker: implements
    SamplePathChecker <.. CustomPathChecker: implements

    SampleReader 
    class SampleReader{
        - pathChecker: SamplePathChecker
        + read(path: str) List~Dict~str, Any~~
    }
    class SamplePathChecker{
        <<Interface>>
        + isValid(path: str) bool
        + getImagePaths(path: str) List~str~
        + getCsvPath(path: str) str
    }
```

## Resources

### Mocking
- [Pytest Mock](https://github.com/pytest-dev/pytest-mock/)
- [Unittest Mock](https://docs.python.org/3/library/unittest.mock.html#patch-object)

### Pytest
- [Skipping Test Cases](https://docs.pytest.org/en/7.1.x/how-to/skipping.html)

## Warning !!!
 This repo is currently under maintenance, converting the boring jupyter notebooks into much more cooler Dash application.