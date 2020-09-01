package gov.gsa.give.ipp.usps.model;

import com.fasterxml.jackson.annotation.JsonAlias;

public class Country {

    @JsonAlias("country_id")
    private int countryId;

    @JsonAlias("country_iso_code")
    private String countryIsoCode;

    @JsonAlias("country_alias")
    private String countryName;

    @JsonAlias("country_abbreviation2")
    private String countryAbbreviation2;

    @JsonAlias("country_abbreviation3")
    private String countryAbbreviation3;
}