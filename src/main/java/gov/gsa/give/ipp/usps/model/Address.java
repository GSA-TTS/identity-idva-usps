package gov.gsa.give.ipp.usps.model;

import com.fasterxml.jackson.annotation.JsonAlias;

import lombok.AllArgsConstructor;
import lombok.Getter;

@Getter
@AllArgsConstructor
public class Address {
    
    private String city;
    private Country country;

    @JsonAlias("address_line_1")
    private String addressLine1;

    @JsonAlias("address_line_2")
    private String addressLine2;

    @JsonAlias("state_province")
    private String stateOrProvince;

    @JsonAlias("postal_code")
    private String postalCode;
}