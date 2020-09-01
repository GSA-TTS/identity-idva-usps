package gov.gsa.give.ipp.usps.service;

import java.time.Duration;
import java.util.List;
import java.util.UUID;

import javax.annotation.PostConstruct;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.ExchangeStrategies;
import org.springframework.web.reactive.function.client.WebClient;

import gov.gsa.give.ipp.usps.model.IppApplicantRequest;
import gov.gsa.give.ipp.usps.model.IppFacilityListRequest;
import gov.gsa.give.ipp.usps.model.PostOffice;
import gov.gsa.give.ipp.usps.model.ProofingResult;
import reactor.core.publisher.Mono;

@Service
public class UspsIppService {

    @Value("${usps.endpoint}")
    private String uspsEndpoint;

    @Value("${usps.request-timeout}")
    private Duration requestTimeout;

    private WebClient client;

    @PostConstruct
    public void init() {
        client = WebClient
            .builder()
            .baseUrl(uspsEndpoint)
            .defaultHeader(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE)
            .exchangeStrategies(ExchangeStrategies
                .builder()
                .codecs(clientCodecConfigurer -> clientCodecConfigurer.defaultCodecs()
                    .enableLoggingRequestDetails(true))
                    .build())
            .build();
    }

    /**
     * Submits a request to the USPS API to search for post offices near a supplied address. 
     * @param request the address to run a search against.
     * @return a list of post offices near the given address with hours, parking, and contact information.
     */
    public Mono<List<PostOffice>> getIppFacilityList(IppFacilityListRequest request) {

        // Use this snippet as a guide.
        // return client
        // .post()
        // .body(Mono.just(regInfo), IppApplicantRequest.class)
        // .retrieve()
        // .onStatus(HttpStatus::isError, ClientResponse::createException)
        // .bodyToMono(UspsScore.class);

        throw new UnsupportedOperationException("Needs to be implemented.");
    }

    /**
     * Submits a request to create a new IPP applicant to the USPS API. If the applicant is created
     * successfully, it returns an enrollment code.
     * @param request the PII associated with the applicant.
     * @return the enrollment code associated with the applicant.
     */
    public Mono<String> createIppApplicant(IppApplicantRequest request) {
        throw new UnsupportedOperationException("Needs to be implemented.");
    }

    /**
     * Submits a request to update an IPP applicant to the USPS API. If the applicant is updated
     * successfully, it returns an enrollment code.
     * @param request the PII associated with the applicant.
     * @return the enrollment code associated with the applicant.
     */
    public Mono<String> updateIppApplicant(IppApplicantRequest request) {
        throw new UnsupportedOperationException("Needs to be implemented.");
    }

    /**
     * Submits a request to the USPS API to re-generate an enrollment code. If successful, 
     * it returns a new enrollment code.
     * @param request the {@link UUID} associated with the applicant
     * @return the enrollment code associated with the applicant.
     */
    public Mono<String> resetIppEnrollmentCode(UUID uuid) {
        throw new UnsupportedOperationException("Needs to be implemented.");
    }

    /**
     * Submits a request to the USPS API to obtain the proofing result associated with an IPP event 
     * for a given applicant. It returns the details about the IPP event.
     * @param request the {@link UUID} associated with the applicant.
     * @return the proofing result associated with the event.
     */
    public Mono<ProofingResult> getProofingResults(UUID uuid) {
        throw new UnsupportedOperationException("Needs to be implemented.");
    }
}
