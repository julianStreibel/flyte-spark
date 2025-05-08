```

Trace:

    Traceback (most recent call last):
      File "/usr/local/lib/python3.10/dist-packages/flytekit/core/base_task.py", line 778, in dispatch_execute
        literals_map, native_outputs_as_map = run_sync(
      File "/usr/local/lib/python3.10/dist-packages/flytekit/utils/asyn.py", line 106, in run_sync
        return self._runner_map[name].run(coro)
      File "/usr/local/lib/python3.10/dist-packages/flytekit/utils/asyn.py", line 85, in run
        res = fut.result(None)
      File "/usr/lib/python3.10/concurrent/futures/_base.py", line 458, in result
        return self.__get_result()
      File "/usr/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
        raise self._exception
      File "/usr/local/lib/python3.10/dist-packages/flytekit/core/base_task.py", line 652, in _output_to_literal_map
        raise e
      File "/usr/local/lib/python3.10/dist-packages/flytekit/core/type_engine.py", line 1412, in async_to_literal
        lv = await transformer.async_to_literal(ctx, python_val, python_type, expected)
      File "/usr/local/lib/python3.10/dist-packages/flytekit/types/structured/structured_dataset.py", line 793, in async_to_literal
        return self.encode(ctx, sd, python_type, protocol, fmt, sdt)
      File "/usr/local/lib/python3.10/dist-packages/flytekit/types/structured/structured_dataset.py", line 820, in encode
        sd_model = handler.encode(ctx, sd, structured_literal_type)
      File "/usr/local/lib/python3.10/dist-packages/flytekitplugins/spark/sd_transformers.py", line 51, in encode
        df.write.mode("overwrite").parquet(path=path)
      File "/opt/spark/python/lib/pyspark.zip/pyspark/sql/readwriter.py", line 1656, in parquet
        self._jwrite.parquet(path)
      File "/opt/spark/python/lib/py4j-0.10.9.7-src.zip/py4j/java_gateway.py", line 1322, in __call__
        return_value = get_return_value(
      File "/opt/spark/python/lib/pyspark.zip/pyspark/errors/exceptions/captured.py", line 169, in deco
        return f(*a, **kw)
      File "/opt/spark/python/lib/py4j-0.10.9.7-src.zip/py4j/protocol.py", line 326, in get_return_value
        raise Py4JJavaError(
    py4j.protocol.Py4JJavaError: An error occurred while calling o122.parquet.
    : java.lang.NoClassDefFoundError: software/amazon/awssdk/transfer/s3/progress/TransferListener
    	at java.base/java.lang.Class.forName0(Native Method)
    	at java.base/java.lang.Class.forName(Unknown Source)
    	at org.apache.hadoop.conf.Configuration.getClassByNameOrNull(Configuration.java:2625)
    	at org.apache.hadoop.conf.Configuration.getClassByName(Configuration.java:2590)
    	at org.apache.hadoop.conf.Configuration.getClass(Configuration.java:2686)
    	at org.apache.hadoop.fs.FileSystem.getFileSystemClass(FileSystem.java:3431)
    	at org.apache.hadoop.fs.FileSystem.createFileSystem(FileSystem.java:3466)
    	at org.apache.hadoop.fs.FileSystem.access$300(FileSystem.java:174)
    	at org.apache.hadoop.fs.FileSystem$Cache.getInternal(FileSystem.java:3574)
    	at org.apache.hadoop.fs.FileSystem$Cache.get(FileSystem.java:3521)
    	at org.apache.hadoop.fs.FileSystem.get(FileSystem.java:540)
    	at org.apache.hadoop.fs.Path.getFileSystem(Path.java:365)
    	at org.apache.spark.sql.execution.datasources.DataSource.planForWritingFileFormat(DataSource.scala:454)
    	at org.apache.spark.sql.execution.datasources.DataSource.planForWriting(DataSource.scala:530)
    	at org.apache.spark.sql.DataFrameWriter.saveToV1Source(DataFrameWriter.scala:387)
    	at org.apache.spark.sql.DataFrameWriter.saveInternal(DataFrameWriter.scala:360)
    	at org.apache.spark.sql.DataFrameWriter.save(DataFrameWriter.scala:239)
    	at org.apache.spark.sql.DataFrameWriter.parquet(DataFrameWriter.scala:789)
    	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)
    	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
    	at java.base/java.lang.reflect.Method.invoke(Unknown Source)
    	at py4j.reflection.MethodInvoker.invoke(MethodInvoker.java:244)
    	at py4j.reflection.ReflectionEngine.invoke(ReflectionEngine.java:374)
    	at py4j.Gateway.invoke(Gateway.java:282)
    	at py4j.commands.AbstractCommand.invokeMethod(AbstractCommand.java:132)
    	at py4j.commands.CallCommand.execute(CallCommand.java:79)
    	at py4j.ClientServerConnection.waitForCommands(ClientServerConnection.java:182)
    	at py4j.ClientServerConnection.run(ClientServerConnection.java:106)
    	at java.base/java.lang.Thread.run(Unknown Source)
    Caused by: java.lang.ClassNotFoundException: software.amazon.awssdk.transfer.s3.progress.TransferListener
    	at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(Unknown Source)
    	at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(Unknown Source)
    	at java.base/java.lang.ClassLoader.loadClass(Unknown Source)
    	... 30 more


Message:

    Py4JJavaError: An error occurred while calling o122.parquet.
    : java.lang.NoClassDefFoundError: software/amazon/awssdk/transfer/s3/progress/TransferListener
    	at java.base/java.lang.Class.forName0(Native Method)
    	at java.base/java.lang.Class.forName(Unknown Source)
    	at org.apache.hadoop.conf.Configuration.getClassByNameOrNull(Configuration.java:2625)
    	at org.apache.hadoop.conf.Configuration.getClassByName(Configuration.java:2590)
    	at org.apache.hadoop.conf.Configuration.getClass(Configuration.java:2686)
    	at org.apache.hadoop.fs.FileSystem.getFileSystemClass(FileSystem.java:3431)
    	at org.apache.hadoop.fs.FileSystem.createFileSystem(FileSystem.java:3466)
    	at org.apache.hadoop.fs.FileSystem.access$300(FileSystem.java:174)
    	at org.apache.hadoop.fs.FileSystem$Cache.getInternal(FileSystem.java:3574)
    	at org.apache.hadoop.fs.FileSystem$Cache.get(FileSystem.java:3521)
    	at org.apache.hadoop.fs.FileSystem.get(FileSystem.java:540)
    	at org.apache.hadoop.fs.Path.getFileSystem(Path.java:365)
    	at org.apache.spark.sql.execution.datasources.DataSource.planForWritingFileFormat(DataSource.scala:454)
    	at org.apache.spark.sql.execution.datasources.DataSource.planForWriting(DataSource.scala:530)
    	at org.apache.spark.sql.DataFrameWriter.saveToV1Source(DataFrameWriter.scala:387)
    	at org.apache.spark.sql.DataFrameWriter.saveInternal(DataFrameWriter.scala:360)
    	at org.apache.spark.sql.DataFrameWriter.save(DataFrameWriter.scala:239)
    	at org.apache.spark.sql.DataFrameWriter.parquet(DataFrameWriter.scala:789)
    	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)
    	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
    	at java.base/java.lang.reflect.Method.invoke(Unknown Source)
    	at py4j.reflection.MethodInvoker.invoke(MethodInvoker.java:244)
    	at py4j.reflection.ReflectionEngine.invoke(ReflectionEngine.java:374)
    	at py4j.Gateway.invoke(Gateway.java:282)
    	at py4j.commands.AbstractCommand.invokeMethod(AbstractCommand.java:132)
    	at py4j.commands.CallCommand.execute(CallCommand.java:79)
    	at py4j.ClientServerConnection.waitForCommands(ClientServerConnection.java:182)
    	at py4j.ClientServerConnection.run(ClientServerConnection.java:106)
    	at java.base/java.lang.Thread.run(Unknown Source)
    Caused by: java.lang.ClassNotFoundException: software.amazon.awssdk.transfer.s3.progress.TransferListener
    	at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(Unknown Source)
    	at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(Unknown Source)
    	at java.base/java.lang.ClassLoader.loadClass(Unknown Source)
    	... 30 more
```