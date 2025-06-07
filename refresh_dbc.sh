#!/bin/sh

if [ ! -e ./can2.dbc -o ! -e ./can1.dbc -o ! -e ./can3.dbc ];
then
    echo "usage $0"
    echo "run the scrip inside of ControlUnitLogicOperator/lib/board_dbc"
    exit -1
fi
git pull

cd ./dbcc/ 
make
cd ..

out_dir=./out_lib
rm -rf $out_dir
mkdir $out_dir

create_lib_can_dbc() {
    echo "creating can${1}.h/c"
    ./dbcc/dbcc ./can${1}.dbc
    sed -i "s/pack_message/pack_message_can${1}/" ./can${1}.h
    sed -i "s/pack_message/pack_message_can${1}/" ./can${1}.c

    sed -i "s/print_message/print_message_can${1}/" ./can${1}.h
    sed -i "s/print_message/print_message_can${1}/" ./can${1}.c

    mkdir $out_dir/can${1}
    mv can${1}.h $out_dir/can${1}
    mv can${1}.c $out_dir/can${1}
}

create_lib_can_dbc 1
create_lib_can_dbc 2
create_lib_can_dbc 3

create_lib_can_dbc 1_rg07
create_lib_can_dbc 2_rg07
