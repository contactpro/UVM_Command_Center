// 
// Author:  
// Filename: uvm_template_sequence.sv  
// Version: Demo   
// Description: sequence template for UVM Testbench Builder
// Language: SystemVerilog and UVM Libraries
//
`ifndef PKT_SEQUENCE_SV
`define PKT_SEQUENCE_SV

import uvm_pkg::*;
`include "C:/Users/HP/WORK_UVM/uvm-1.1d/src/uvm_macros.svh"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/uvm_templates/packet_seq_item.sv"

class uvm_template_sequence extends uvm_sequence#(packet_seq_item);
  `uvm_object_utils(uvm_template_sequence)
  
  // constructor
  function new(string name = "uvm_template_sequence", uvm_object parent=null);
    super.new(name);
  endfunction: new
   
  // create, skip randomize, and send the item to driver
  virtual task body();
    repeat(2) begin
      req = packet_seq_item::type_id::create("req");
      wait_for_grant();
      req.addr = 2'b11;
      req.wr_en = 1'b1;
      req.rd_en = 1'b0;
      req.wdata = 8'hea;
      req.rdata = 8'hzz;
      send_request(req);
      wait_for_item_done();
    end 
    repeat(2) begin
      req = packet_seq_item::type_id::create("req");
      rsp = packet_seq_item::type_id::create("rsp");
      wait_for_grant();
      req.addr = 2'b11;
      req.wr_en = 1'b0;
      req.rd_en = 1'b1;
      req.wdata = 8'hzz;
      req.rdata = 8'hzz; 
      send_request(req);
      wait_for_item_done();  // rsp.rdata and req.rdata = vif.rdata;
    end       
  endtask
  
endclass: uvm_template_sequence

//
// write_sequence - "write" type
//
class write_sequence extends uvm_sequence#(packet_seq_item);
  
  `uvm_object_utils(write_sequence)
    
  // constructor
  function new(string name = "write_sequence");
    super.new(name);
  endfunction
  
  virtual task body();
   repeat(2) begin
     req = packet_seq_item::type_id::create("req");
     wait_for_grant();
     req.addr = 2'b11;
     req.wr_en = 1'b1;
     req.rd_en = 1'b0;
     req.wdata = 8'hee;
     req.rdata = 8'hzz;
     send_request(req);
     wait_for_item_done();
   end 
  endtask
endclass
//=========================================================================

//
// read_sequence - "read" type
//
class read_sequence extends uvm_sequence#(packet_seq_item);
  
  `uvm_object_utils(read_sequence)
    
  // constructor
  function new(string name = "read_sequence");
    super.new(name);
  endfunction
  
  virtual task body();
    repeat(2) begin
      req = packet_seq_item::type_id::create("req");
      wait_for_grant();
      req.addr = 2'b11;
      req.wr_en = 1'b0;
      req.rd_en = 1'b1;
      req.wdata = 8'hzz;
      req.rdata = 8'hee;
      send_request(req);
      wait_for_item_done();
    end     
  endtask
endclass
//=========================================================================

//
// write_read_sequence - "write" followed by "read" 
//
class write_read_sequence extends uvm_sequence#(packet_seq_item);
  
  `uvm_object_utils(write_read_sequence)
    
  // constructor
  function new(string name = "write_read_sequence");
    super.new(name);
  endfunction
  
  virtual task body();
    repeat(2) begin
      req = packet_seq_item::type_id::create("req");
      wait_for_grant();
      req.addr = 2'b11;
      req.wr_en = 1'b1;
      req.rd_en = 1'b0;
      req.wdata = 8'hee;
      req.rdata = 8'hzz;
      send_request(req);
      wait_for_item_done();
    end 
    repeat(2) begin
      req = packet_seq_item::type_id::create("req");
      wait_for_grant();
      req.addr = 2'b11;
      req.wr_en = 1'b0;
      req.rd_en = 1'b1;
      req.wdata = 8'hzz;
      req.rdata = 8'hee;
      send_request(req);
      wait_for_item_done();
    end     
  endtask

endclass: write_read_sequence

`endif

