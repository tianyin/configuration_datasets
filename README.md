#Configuration Datasets

We release the datasets we used to study the configuration practices and issues of real-world users. Some of the findings are summarized in the paper,

T. Xu, L. Jin, X. Fan, Y. Zhou, S. Pasupathy, and R. Talwadker, Hey, You Have Given Me Too Many Knobs! ---Understanding and Dealing with Over-Designed Configuration in System Software, Proceedings of the 10th Joint Meeting of the European Software Engineering Conference and the ACM SIGSOFT Symposium on the Foundations of Software Engineering (ESEC/FSE'15), Oct. 31-Sep. 4, 2015, Bergamo, Italy. [[Download] (http://cseweb.ucsd.edu/~tixu/papers/fse15.pdf)]

Please cite the paper if you use the datasets :-)

#What is included in the datasets?

The datasets contain two subsets, the _configuration files_ used by real-world users and the _configuration issues_ encountered by the users. The former can help studies on the users' practices in configuring software systems, while the latter can help studies on the user's difficulties and errors during their configuration tasks.

The layout of the dataset:

1. `configfiles`: this directory contains the datasets of the configuration files

2. `configissues`: this directory contains the datasets of the configuration issues

#What is the scale of the datasets?

##configfiles
The `configfiles` dataset contains configuration files of two software systems, Apache HTTP server (httpd) (http://httpd.apache.org/) and MySQL database server (https://www.mysql.com/).

In our study, we only used specific versions of httpd and MySQL, i.e., httpd-2.2.x and mysqld-5.x. But the dataset contains the configuration files of all the versions we collected. 

| Software      | Version   | #files    |
| ------------- |:---------:| ---------:|
| httpd         | all       | 311       |
| httpd         | 2.2.x     | 168       |
| mysqld        | all       | 823       |
| mysqld        | 5.x       | 260       |

Only the files we studied (httpd-2.2.x and mysqld-5.x) are included in the datasets. For the rest, we provide you with the link so you can download them directly if you needed.

##configissues
The `configissues` dataset contains the issues of three software projects, Apache HTTP server (http://httpd.apache.org/), MySQL (https://www.mysql.com/), and Hadoop (https://hadoop.apache.org/).

| Software      |  #issues  |
| ------------- |:---------:|
| httpd         |  97       |
| mysqld        |  96       |
| hadoop        |  98       |

Note that we do not consider version in this datasets, which means an issue could be from any version of the software.

#How did we collect the datasets?

Please refer to the paper. Basically, all the files are collected from the web, including Q&A forums and the official mailing lists of the software, including

1. StackOverflow (http://stackoverflow.com/)

2. ServerFault (http://serverfault.com/)

3. Pro Webmasters (http://webmasters.stackexchange.com/)

4. Database Administrators (http://dba.stackexchange.com/)

5. MYSQL General List (<mysql@lists.mysql.com>)

6. MySQL on Win32 (<win32@lists.mysql.com>)

7. MySQL Cluster (<cluster@lists.mysql.com>)

8. MySQL Replication (<replication@lists.mysql.com>)

9. MySQL Backup (<backup@lists.mysql.com>)

10. InnoDB Storage Engine (<innodb@lists.mysql.com>)

11. Apache HTTP Server Users Mailing Lists (<users@httpd.apache.org>)

12. Hadoop User Mailing Lists (<user@hadoop.apache.org>)

Believe or not, we crawled/downloaded the entire mailing list archives and online posts with specific tags from the first mail/post to the most recent ones at the collection period. The collection is conducted during January to March in 2014. We automatically parsed the entire mailing list archives and all the posts on the above sources via a number of filter pipelines. At the end of the pipeline, we manually collect the files from the sources.

The issue dataset was collected from the same sources. We used a rolling-based sampling methods to get the datasets, which means we didn't look at all the mail threads/posts (which is not possible).

#How can you use the datasets?
The instruction of the file format and layout can be found in the README in the dataset folders.

#Warning
When using the dataset, you have to be aware that the datasets only contain information about parameter-based configurations. It does not contain configuration issues or practices such as compatibility or components. In other words, it reflects a subset of the whole problem.
