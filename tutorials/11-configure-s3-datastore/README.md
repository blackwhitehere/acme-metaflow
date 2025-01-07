# Episode 11-configure-s3-datastore

#### Shows how to setup metaflow to use S3 Datastore

- We will generate temporary credentials to access an S3 Bucket
- We will configure the S3 Bucket as a Metaflow Datastore
- We will execute a flow that saves its artifacts to the S3 Datastore.

### Using broad access permissions for AWS access.

This method uses broad access permissions granted to a user with `PowerUserAccess` template from AWS IAM Identity Center. Temporary credentials to access AWS are generated which improves security posture but requires to periodically refresh the credentials.

#### Pre-requisites:

1. An AWS Account with s3 bucket e.g. `s3://acme-s3-dev` to which you have `PowerUserAccess` as defined by AWS IAM Identity Center.
1. Run `chmod +x .admin/*` if scripts there don't have execute permissions yet.

#### Configure local access to AWS using PowerUserAccess:
1. Install AWS CLI [Link](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
1. AWS Account admininstrator needs to provision an account for you via IAM Identity Center. Login to the Access Portal via a provided link.
1. Set `AWS_ACCOUNT_ID`, `AWS_SSO_REGION` and `AWS_SSO_START_URL` in `.env` file in root of the repo from the values in the access portal under "Access keys".
1. Add the bucket name (together with `s3://` prefix) to `.env` file under `TEST_AWS_BUCKET_NAME`. 
1. From root of the repo run `./admin/one_time_aws_sso_setup.sh` and supply required details. Name the auth profile e.g. `default` and add to `.env` file `AWS_PROFILE=default`. You can see configured aws authentication profiles under `~/.aws/config`
1. From root of the repo run `./admin/refresh_credentials.sh` when your temporary credentials expire.
1. Run `./admin/test_s3_access.sh` which should print contents of the bucket in `TEST_AWS_BUCKET_NAME` by using temporary credentials.

### Assuming granular role

This method uses narrow access permissions granted to a role named e.g. `MetaflowUserRole`. Temporary credentials to access S3 are generated which improves security posture but requires to periodically refresh the credentials.

#### Pre-requisites:

1. Run `chmod +x .admin/*` if scripts there don't have execute permissions yet.
1. An AWS Account with s3 bucket e.g. `s3://acme-s3-dev`.
1. IAM role named e.g. `MetaflowUserRole` with attached policy named e.g. `MetaflowS3DataStoreAcmeDev` with contents like so:

        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "MetaflowS3DataStoreAcmeDev",
                    "Effect": "Allow",
                    "Action": [
                        "s3:*Object",
                        "s3:ListBucket"
                    ],
                    "Resource": [
                        "arn:aws:s3:::acme-s3-dev/*",
                        "arn:aws:s3:::acme-s3-dev"
                    ]
                }
            ]
        }

and "Trust relationship" that allows the IAM Identity Center user to assume the role like so:

        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "MetaflowUserRole",
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": "arn:aws:sts::<Account ID>:assumed-role/AWSReservedSSO_PowerUserAccess_<Unique ID>/<IAM Identity Center username>"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }

#### Configure local access to AWS using granural role

1. Add `METAFLOW_USER_ROLE=MetaflowUserRole` to `.env` file.
1. Execute all steps from `Configure local access to AWS using PowerUserAccess` but instead of using `./admin/refresh_credentials.sh` to re-generate the credentials use `./admin/assume_role.sh`.
1. Run `./admin/test_s3_access.sh` which should print contents of the bucket in `TEST_AWS_BUCKET_NAME` by using temporary credentials.

### Configure the S3 Bucket as a Metaflow Datastore
1. Configure local client to use S3 as a Datastore by calling `metaflow configure aws` and provide bucket name `s3://acme-s3-dev` when prompted to configure the storage backend. Skip configuration of other options when prompted. For more info see [Link](https://docs.outerbounds.com/engineering/operations/configure-metaflow/)

You should see then the following values in `~/.metaflowconfig/config.json`:

        "METAFLOW_DATASTORE_SYSROOT_S3": "s3://acme-s3-dev",
        "METAFLOW_DATATOOLS_S3ROOT": "s3://acme-s3-dev/data",
        "METAFLOW_DEFAULT_DATASTORE": "s3",

### To play this episode:
1. ```cd tutorials```
1. ```python 00-helloworld/helloworld.py run```

You can now view artficats created by flow run being saved to S3 instead of local storage.