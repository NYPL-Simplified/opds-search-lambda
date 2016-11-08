# opds-search-lambda
An AWS Lambda function for getting results from Elasticsearch as OPDS.

This function uses an Elasticsearch index created with [a script from the LS Open Access Content Server](https://github.com/NYPL-Simplified/content_server/blob/master/bin/util/create_static_feed)

## Installation
This repository depends on the [LS Server Core](https://github.com/NYPL-Simplified/server_core) as a git submodule.

Run `git submodule init && git submodule update` after cloning to initialize core.

Create a virtual environment in `env` and run `pip install -r requirements.txt` to install dependencies.

Copy `config.py.sample` to `config.py` and fill in the Elasticsearch url and index to use.

Run `bin/create_deployment_package <zip_file_name>` to create a zip file to upload to AWS lambda.

Note: this must be created on amazon linux ec2 instance to work on aws. Run `sudo yum install libxml2-devel libxslt-devel gcc libxslt-python` to set up dependencies.


## License

```
Copyright © 2016 The New York Public Library, Astor, Lenox, and Tilden Foundations

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
