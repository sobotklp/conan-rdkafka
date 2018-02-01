#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <inttypes.h>

#include "rdkafka.h"

///////////////////////////////////////////
// In the test file
#include <gtest/gtest.h>

TEST(rdkafkaTest, Static) {
    rd_kafka_conf_t *conf;
    conf = rd_kafka_conf_new();
    rd_kafka_conf_destroy(conf);
}
