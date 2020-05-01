import os

from aws_cdk import (
    core,
    aws_certificatemanager as acm,
)


class SiteCertificate(acm.Certificate):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(
            scope,
            id,
            domain_name=os.environ.get("DOMAIN_NAME", "mysite.com"),
            validation_method=acm.ValidationMethod.DNS,
            subject_alternative_names=[
                f"*.{os.environ.get('DOMAIN_NAME', 'mysite.com')}"
            ],
            **kwargs,
        )
