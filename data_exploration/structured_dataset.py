""" Class design for Dataset"""

#import pickle
import pandas as pd

from data_exploration.dataset import AbstractDataset
#from data_exploration.dataset_explorer import Explorer
from data_exploration.dataset_type import DatasetType
from data_exploration.dataSet_Versioning import PachydermRepoManager as pc
# from xpresso.ai.core.logging.xpr_log import XprLogger
#from csvdiff import diff_records

__all__ = ['StructuredDataset']
__author__ = 'Srijan Sharma'


# This is indented as logger can not be serialized and can not be part
# of dataset
# logger = XprLogger()


class StructuredDataset(AbstractDataset):
    """ StructuredDataset stores the data in tabular format. It reads data
    from csv, excel or any database. It stores the dataset into local storage
    in pickle format."""

    def __init__(self, dataset_name: str = "default",
                 description: str = "This is a structured dataset"):
        super().__init__(dataset_name=dataset_name,
                         description=description)

        self.type = DatasetType.STRUCTURED

    def import_dataset(self, data_source, local_storage_required: bool = False,
                       sample_percentage: float = 100):
        """ Fetches dataset from multiple data sources and loads them
        into a dataset"""
        self.data = pd.read_csv(data_source)
        print('We are trying')
        pc.push_dataset(self,dataset=self.data, description="Jagannath")
        #self.local_storage_required = local_storage_required
        #self.sample_percentage = sample_percentage


if __name__ == "__main__":
    dataset = StructuredDataset()
    dataset.import_dataset("age_count.csv")
    """
    explorer = Explorer(dataset)
    explorer.understand()
    explorer.explore_attributes()

    dataset2 = StructuredDataset()
    dataset2.import_dataset("./config/test/data/test.csv")
    explorer = Explorer(dataset2)
    explorer.understand()
    explorer.explore_attributes()

    dataset.diff(dataset2)

    for val in dataset.info.attributeInfo:
        if "ordinal" in val.name.lower():
            val.type = "ordinal"

    explorer.explore_metrics()
    for val in dataset.info.attributeInfo:
        print("Name : {} , Dtype : {} ,  Type : {} , Metrics : {} \n".format(
            val.name, val.dtype, val.type, val.metrics))
            
            """
