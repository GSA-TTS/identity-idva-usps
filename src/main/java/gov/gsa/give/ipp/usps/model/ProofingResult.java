package gov.gsa.give.ipp.usps.model;

import java.time.Instant;
import java.util.Date;

import com.fasterxml.jackson.annotation.JsonProperty;

import lombok.Getter;

@Getter
public class ProofingResult {
    private String status;
    private String failureReason;
    private String locationType;
    private String proofingPostOffice;
    private String proofingCity;
    private String proofingState;
    private String enrollmentCode;
    private String primaryIdType;
    private Instant transactionStartDateTime;
    private Instant transactionEndDateTime;
    private String secondaryIdType;
    private String fraudSuspected;
    private String proofingConfirmationNumber;
    private AccountName accountName;
    private Address address;
    private Date birthDate;

    @JsonProperty("IPPVersion")
    private String ippVersion;

    
}