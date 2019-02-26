#!/usr/bin/python
#
# test_basic_flow.py
#
# This source file is part of the FoundationDB open source project
#
# Copyright 2013-2019 Apple Inc. and the FoundationDB project authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# MongoDB is a registered trademark of MongoDB, Inc.
#


def test_simple_coll_index(fixture_collection):
    collection = fixture_collection

    # Create an index
    collection.create_index('a', name='idx_a')

    # Insert bunch of documents
    docs = []
    for i in range(1, 50):
        docs.append({'a': i, 'b': str(i)})
    collection.insert_many(docs)

    # Create another index
    collection.create_index('b')

    # Query and check results
    returned = collection.find({'a': {'$gt': 10, '$lt': 21}}).count()
    assert returned == 10, "Expected: 10, Received: {}".format(returned)

    # Drop an index
    collection.drop_index('idx_a')

    # Query and check results
    returned = collection.find({'a': {'$gt': 10, '$lt': 21}}).count()
    assert returned == 10, "Expected: 10, Received: {}".format(returned)

    # Drop all indexes
    collection.drop_indexes()

    # Query and check results
    returned = collection.find({'a': {'$gt': 10, '$lt': 21}}).count()
    assert returned == 10, "Expected: 10, Received: {}".format(returned)
