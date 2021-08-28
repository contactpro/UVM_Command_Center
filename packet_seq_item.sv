// 
// Author:  
// Filename: packet_seq_item.sv  
// Version: Demo   
// Description: packet_seq_item template for UVM Testbench Builder
// Language: SystemVerilog and UVM Libraries.
//
`ifndef PKT_SEQ_ITEM_SV
`define PKT_SEQ_ITEM_SV

import uvm_pkg::*;
`include "C:/Users/HP/WORK_UVM/uvm-1.1d/src/uvm_macros.svh"

class packet_seq_item extends uvm_sequence_item;
  //
  // RAND and Constrained only with UVM Sim License,
  // therefore, architect directed seq_item 
  // 
  // data and control fields
  //
  // rand bit [1:0] addr;
  // rand bit       wr_en;
  // rand bit       rd_en;
  // rand bit [7:0] wdata;
  //      bit [7:0] rdata;
  // 
  bit [1:0] addr;
  bit       wr_en;
  bit       rd_en;
  bit [7:0] wdata;
  bit [7:0] rdata;  

  // utility and field macros
  `uvm_object_utils_begin(packet_seq_item)
    `uvm_field_int(addr,UVM_ALL_ON)
    `uvm_field_int(wr_en,UVM_ALL_ON)
    `uvm_field_int(rd_en,UVM_ALL_ON)
    `uvm_field_int(wdata,UVM_ALL_ON)
    `uvm_field_int(rdata,UVM_ALL_ON)    
  `uvm_object_utils_end
  
  // constructor
  function new(string name = "packet_seq_item", uvm_object parent=null);
    super.new(name);
  endfunction: new  

  // constraint, to generate any one among write and read
  // constraint wr_rd_c { wr_en != rd_en; }; 
  
endclass: packet_seq_item

`endif

