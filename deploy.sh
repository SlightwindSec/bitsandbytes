#!/bin/bash
CURRENT_DIR=$(
    cd $(dirname ${BASH_SOURCE:-$0})
    pwd
)
cd $CURRENT_DIR

BUILD_TYPE="Release"
INSTALL_PREFIX="${CURRENT_DIR}/out"
SOC_VERSION="Ascend910B4"

source ${ASCEND_TOOLKIT_HOME}/bin/setenv.bash

set -e
rm -rf build out
mkdir -p build
cmake -B build \
    -DSOC_VERSION=${SOC_VERSION} \
    -DCMAKE_BUILD_TYPE=${BUILD_TYPE} \
    -DCMAKE_INSTALL_PREFIX=${INSTALL_PREFIX} \
    -DASCEND_CANN_PACKAGE_PATH=${ASCEND_TOOLKIT_HOME} \
    -DCOMPUTE_BACKEND=npu

cmake --build build -j
cmake --install build
