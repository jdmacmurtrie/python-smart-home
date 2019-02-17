# Smart Home Interface

Smart Home Interface is an experiment in Python command line tools.  Utilizing the data given, it seeks to simulate a tool with which a user can access information about smart devices within an apartment building.  A user may only access the tool if they exist in the data in the `property_data.json` file.  From there, the information is restricted based on the users role as 'admin' or 'resident'.  An admin may move a resident in or out on an apartment, and the new data will be copied into `property_data_copy.json`.

## Getting Started

In order to run this program locally, you must Python3 installed.
```
$ python3 --version
=> Python 3.6.7
```

### Run the Program

In order to run the tool, run the following command in your terminal:

```sh
$ python3 smart_home_interface.py
```
