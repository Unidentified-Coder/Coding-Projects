export default class Country {
    code;
    name;
    continent;
    region;
    SurfaceArea;
    IndepYear;
    population;
    LifeExpectancy;
    GNP;
    GNPOld;
    LocalName;
    GovernmentForm;
    HeadOfState;
    Capital;
    Code2;

    constructor(code, name, continent, region, SurfaceArea, IndepYear, population, LifeExpectancy, GNP, GNPOld, LocalName, GovernmentForm, HeadOfState, Capital, Code2 ) {
        this.code = code;
        this.name = name;
        this.continent = continent;
        this.region = region;
        this.SurfaceArea = SurfaceArea;
        this.IndepYear = IndepYear;
        this.population = population;
        this.LifeExpectancy = LifeExpectancy;
        this.GNP = GNP;
        this.GNPOld = GNPOld;
        this.LocalName = LocalName;
        this.GovernmentForm = GovernmentForm;
        this.HeadOfState = HeadOfState;
        this.Capital = Capital;
        this.Code2 = Code2;
    }
}