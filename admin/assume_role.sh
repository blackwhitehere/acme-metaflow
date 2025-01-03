# Load environment variables from .env file
set -o allexport
source .env
set +o allexport

# Step 1: Assume the role again to get new credentials
account_id=$1
if [ -z "$account_id" ]; then
    account_id=$AWS_ACCOUNT_ID
fi

role_name=$2
if [ -z "$role_name" ]; then
    role_name=$METAFLOW_USER_ROLE
fi
assume_role_output=$(aws sts assume-role --role-arn arn:aws:iam::$account_id:role/$role_name --role-session-name $(openssl rand -hex 12) --profile $AWS_CLI_PROFILE)

# Step 2: Export the new temporary credentials
export AWS_ACCESS_KEY_ID=$(echo $assume_role_output | jq -r '.Credentials.AccessKeyId')
export AWS_SECRET_ACCESS_KEY=$(echo $assume_role_output | jq -r '.Credentials.SecretAccessKey')
export AWS_SESSION_TOKEN=$(echo $assume_role_output | jq -r '.Credentials.SessionToken')