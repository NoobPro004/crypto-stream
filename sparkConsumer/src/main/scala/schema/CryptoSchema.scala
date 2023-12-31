package schema

import org.apache.spark.sql.types.{DataTypes, StructType}


object CryptoSchema {

  val schema: StructType = new StructType()
    .add("name_coin", DataTypes.StringType )
    .add("symbol_coin", DataTypes.StringType)
    .add(name="uuid", DataTypes.StringType)
    .add("volume", DataTypes.LongType)
    .add("market_cap", DataTypes.LongType)
    //price is casted separately to Double from String
    .add("price", DataTypes.StringType)
    .add("percent_change_24hr", DataTypes.DoubleType)
    .add("timestamp", DataTypes.TimestampType)

}