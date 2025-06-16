The scripts in this directory are meant for pre-seeding localstack with custom state. For example, creating certain AWS resources when starting up the localstack container.

This is done with localstack initialization hooks. See the docs [here](https://docs.localstack.cloud/references/init-hooks/).

In order for this to run properly, the `init-aws.sh` script needs to be executable:
```
chmod +x init-aws.sh
```

Then once you start up the localstack container, the script will be executed during the `ready` stage and your AWS resources will be created.