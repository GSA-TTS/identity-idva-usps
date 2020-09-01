package gov.gsa.give.ipp.usps.model;

import lombok.AllArgsConstructor;
import lombok.Getter;

@Getter
@AllArgsConstructor
public class IppFacilityListRequest {
    private String streetAddress;
    private String city;
    private String state;
    private String zipCode;
}