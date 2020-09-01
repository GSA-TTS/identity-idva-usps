package gov.gsa.give.ipp.usps.model;

import lombok.Getter;

@Getter
public class PostOffice {
    private String name;
    private String streetAddress;
    private String city;
    private String state;
    private String zip5;
    private String zip4;
    private String parking;
    private String distance;
    private String weekdayHours;
    private String saturdayHours;
    private String sundayHours;
    private String phone;
}