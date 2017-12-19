# B2 - notes

## What we have
* three mails, hashed and then enveloped
* Bob's private key (keyrec..)
* Bob's cert (certec..)
* CA cert used for signing Bob's cert (CAcert.pem)

## `openssl cms` take-aways
* `-recip file` - when decrypting, specify recipients cert.
* `-CAfile file`
	  a file containing trusted CA certificates, only used with -verify.
* `-inkey file`
	the private key to use when signing or decrypting. This must match the corresponding certificate.

## Decrypting envelopment part

Following command gave headers of message, probably smth good. Halfay through?
	openssl cms -decrypt -in mail3.msg -inkey keyreceiver.pem -no_signer_cert_verify-CApath certs

`openssl cms -decrypt -in mail2.msg -inkey keyreceiver.pem -no_signer_cert_verify -CApath certs -out headers/mail2.head`

Wrote all to a header/ dir.

## Verifying digest part

`openssl cms -digest_verify -in mail1.head -inkey ../keyreceiver.pem -no_signer_cert_verify -CApath ../certs/ -out ../verified/mail1.verif |& tee -a ../verified/mail1.verif`
Content-Type: text/plain

Hey Bob. EITN41 rocks!
**Verification successful**

$ ...
Content-Type: text/plain

Hey Bob. EITN41 kicks some serious ass!
Verification failure
4294956672:error:2E07509E:CMS routines:cms_DigestedData_do_final:verification failure:cms_dd.c:131:

$ ...
Content-Type: text/plain

Hey Bob. EITN41 is the shit!
Verification failure
4294956672:error:2E07509E:CMS routines:cms_DigestedData_do_final:verification failure:cms_dd.c:131:


