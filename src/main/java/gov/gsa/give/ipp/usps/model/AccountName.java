package gov.gsa.give.ipp.usps.model;

import com.fasterxml.jackson.annotation.JsonAlias;

import lombok.AllArgsConstructor;
import lombok.Getter;

@Getter
@AllArgsConstructor
public class AccountName {
    
    @JsonAlias("first_name")
    private String firstName;
    
    @JsonAlias("middle_initial")
    private String middleInitial;

    @JsonAlias("last_name")
    private String lastName;
}