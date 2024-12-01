from metaflow import FlowSpec, Parameter, step, JSONType, IncludeFile

from datetime import datetime
import json

def deployment_info(context):
    return json.dumps({'who': context.user_name,
                       'when': datetime.now().isoformat()})

class ParameterFlow(FlowSpec):
    """Shows how to use parameters in Metaflow."""

    alpha = Parameter('alpha',
                      help='Learning rate',
                      required=False,
                      default=0.01)
    
    gdp = Parameter('gdp',
                    help='Country-GDP Mapping',
                    type=JSONType,
                    default='{"US": 1939}')
    
    # https://docs.metaflow.org/production/scheduling-metaflow-flows/scheduling-with-argo-workflows#deploy-time-parameters
    # https://docs.metaflow.org/api/flowspec#deploy-time-parameters
    info = Parameter('deployment_info',
                     type=JSONType,
                     default=deployment_info)
    
    myfile = IncludeFile(
        'myfile',
        is_text=False,
        help='My input file',
        default='myfile.txt')

    @step
    def start(self):
        """Prints values of parameters"""
        print('alpha is %f' % self.alpha)
        print('The GDP of US is $%dB' % (self.gdp["US"]))
        print('This flow was deployed at %s by %s'\
              % (self.info['when'], self.info['who']))
        print(f"The contents of myfile are: {self.myfile}")
        self.next(self.end)

    @step
    def end(self):
        print('alpha is still %f' % self.alpha)

if __name__ == '__main__':
    ParameterFlow()