export default class CountryLanguage {
    CountryCode;
    Language;
    IsOfficial;
    Percentage;

    constructor(CountryCode, Language, IsOfficial, Percentage) {
        this.CountryCode = CountryCode;
        this.Language = Language;
        this.IsOfficial = IsOfficial;
        this.Percentage = Percentage;
    }
}