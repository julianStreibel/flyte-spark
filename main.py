import flytekit
from flytekit import ImageSpec, task, workflow, Resources
from flytekitplugins.spark import Spark
from pyspark.sql import DataFrame


custom_image = ImageSpec(
    registry="211125663991.dkr.ecr.us-west-2.amazonaws.com",
    name="flytekit",
    packages=[
        # Needed for IPv6 support
        "flytekit",
        "flytekitplugins-spark",
        "pyspark==3.4.0",
    ],
    pip_extra_args="--pre",
    platform="linux/arm64",
)


@task(
    task_config=Spark(),
    container_image=custom_image,
    requests=Resources(cpu="100m", mem="1000M"),
    limits=Resources(cpu="200m", mem="2000M"),
)
def hello_spark() -> DataFrame:
    """Create a dummy dataframe using the spark session from flytekit."""
    spark = flytekit.current_context().spark_session
    df = spark.createDataFrame([(1, "foo"), (2, "bar")], ["id", "value"])
    return df


@task(
    task_config=Spark(),
    container_image=custom_image,
    requests=Resources(cpu="100m", mem="1000M"),
    limits=Resources(cpu="200m", mem="2000M"),
)
def show_df(df: DataFrame):
    """Print the dataframe."""
    df.show()


@workflow
def hello_spark_wf():
    """Run the hello spark workflow."""
    df = hello_spark()
    show_df(df=df)


if __name__ == "__main__":
    hello_spark_wf()
