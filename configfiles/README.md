## Configuration File Dataset

There are two folders corresponding to httpd and mysql respectively.

In each folder, `all_versions.metadata.csv` describes all the configuration files and `$version.metadata.csv` describes the particular version (i.e., httpd-2.2.x and mysqld-5.x). The configuration files of ``$version.metadata.csv` is included in the same directory as the metadata files.

The format of `all_versions.metadata.csv` is:
"``VERSION,LINK,DESC,SOURCE``"

The format of `$version.metadata.csv` is:
"``FILENAME,VERSION,LINK,DESC,SOURCE``"

The only difference is that `$version.metadata.csv` contains the file name pointing to the files, while `all_versions.metadata.csv` does not include the files.

Recently, we also add the configurations of Hadoop and HBase, which has different file format. Please see the docs in `hadoop+hbase` for details.
