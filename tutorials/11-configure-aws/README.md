# Episode 11-configure-aws

**Shows how to setup AWS account with two essential resources for using metaflow: S3 based Datastore and DB based Metadata Provider**

- We will configure AWS as a metaflow backend.
- We will first focus just on two essential elements of metaflow stack: S3 based Datastore and DB based Metadata Provider


#### To play this episode:
1. Install AWS CLI -- Link
1. AWS Account admininstrator needs to provision an account for you via IAM Identity Center. Login to the portal via a provided link.
1. Set `AWS_ACCOUNT_ID`, `AWS_SSO_REGION` and `AWS_SSO_START_URL`
1. From root of the repo run `./admin/one_time_aws_sso_setup.sh` to configure login details from IAM Identity Center Access Portal. Name profile name `default` and add to `.env` file `AWS_CLI_PROFILE=default`
1. From root of the repo run `./admin/refresh_credentials.sh` when your temporary credentials expire.
1. Configure local client to use AWS configuration [Link](https://docs.outerbounds.com/engineering/operations/configure-metaflow/) with `metaflow configure aws` and provide bucket name s3://acme-s3-dev.