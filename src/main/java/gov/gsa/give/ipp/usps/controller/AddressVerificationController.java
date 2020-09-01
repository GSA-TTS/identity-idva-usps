package gov.gsa.give.ipp.usps.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import gov.gsa.give.ipp.usps.model.IppApplicantRequest;
import gov.gsa.give.ipp.usps.service.UspsIppService;
import reactor.core.publisher.Mono;

@RestController
public class AddressVerificationController {

    @Autowired
    private UspsIppService uspsHttpService;

    @PostMapping("/applicant")
    public Mono<String> post(@RequestBody IppApplicantRequest request) {
        return uspsHttpService.createIppApplicant(request);
    }

    @PutMapping("/applicant")
    public Mono<String> put(@RequestBody IppApplicantRequest request) {
        return uspsHttpService.updateIppApplicant(request);
    }
}
