// 
// Author:  
// Filename: uvm_template_scoreboard.sv  
// Version: Demo   
// Description: scoreboard template for UVM Testbench Builder
// Language: SystemVerilog and UVM Libraries
//
`ifndef PKT_SCOREBOARD_SV
`define PKT_SCOREBOARD_SV

import uvm_pkg::*;
`include "C:/Users/HP/WORK_UVM/uvm-1.1d/src/uvm_macros.svh"

`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/BUILD_TEST/UVM_COMMAND_CENTER_v1.8/packet_seq_item.sv"

class uvm_template_scoreboard extends uvm_scoreboard;
  `uvm_component_utils(uvm_template_scoreboard) 
  
  // declaring pkt_qu to store the pkt's received from monitor
  packet_seq_item pkt_qu[$];
  
  // sc_mem 
  bit [7:0] sc_mem [4];

  //port to receive DUT INPUT (WRITE) and DUT OUTPUT (READ) packets from monitor
  uvm_analysis_imp #(packet_seq_item, uvm_template_scoreboard) item_collected_export;
  
  // constructor 
  function new (string name="uvm_template_scoreboard", uvm_component parent=null);
    super.new(name, parent);
  endfunction : new

  // phase progress information funtion
  function void phase_started(uvm_phase phase);
    `uvm_info("SCOREBOARD_PHASE_STATUS", $sformatf("Phase started for %s", phase.get_name()), UVM_NONE);
  endfunction: phase_started

  // build_phase - create port and initialize local memory
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
      `uvm_info("SCBD_BUILD_PHASE","In SCBD BUILD PHASE . . .", UVM_MEDIUM);
      item_collected_export = new("item_collected_export", this);
      foreach(sc_mem[i]) sc_mem[i] = 8'hFF;
  endfunction: build_phase
  
  // connect phase
  virtual function void connect_phase(uvm_phase phase);
    super.connect_phase(phase);
  endfunction: connect_phase  
    
  // write function
  // receives the pkt from monitor and pushes into queue
  virtual function void write(packet_seq_item pkt);
    pkt.print();
    pkt_qu.push_back(pkt);
    `uvm_info("SCBD_PKT_WRITE_TO_QUEUE","SCBD Receives PKT via push_back from QUEUE . . .", UVM_MEDIUM);
  endfunction : write

  // run_phase - compare's the read data with the expected data(stored in local memory)
  // local memory will be updated on the write operation.
  virtual task run_phase(uvm_phase phase);
    packet_seq_item mem_pkt;
    `uvm_info("SCBD_RUN_PHASE","In SCBD RUN PHASE . . .", UVM_MEDIUM);
    forever begin
      wait(pkt_qu.size() > 0);
      mem_pkt = pkt_qu.pop_front();

      if(mem_pkt.wr_en) begin
        sc_mem[mem_pkt.addr] = mem_pkt.wdata;
        `uvm_info(get_type_name(),$sformatf("------ :: WRITE DATA       :: ------"),UVM_LOW)
        `uvm_info(get_type_name(),$sformatf("Addr: %0h",mem_pkt.addr),UVM_LOW)
        `uvm_info(get_type_name(),$sformatf("Data: %0h",mem_pkt.wdata),UVM_LOW)
        `uvm_info(get_type_name(),"------------------------------------",UVM_LOW)        
      end
      else if(mem_pkt.rd_en) begin
        if(sc_mem[mem_pkt.addr] == mem_pkt.rdata) begin
          `uvm_info(get_type_name(),$sformatf("------ :: READ DATA Match :: ------"),UVM_LOW)
          `uvm_info(get_type_name(),$sformatf("Addr: %0h",mem_pkt.addr),UVM_LOW)
          `uvm_info(get_type_name(),$sformatf("Expected Data: %0h Actual Data: %0h",sc_mem[mem_pkt.addr],mem_pkt.rdata),UVM_LOW)
          `uvm_info(get_type_name(),"------------------------------------",UVM_LOW)
        end
        else begin
          `uvm_error(get_type_name(),"------ :: READ DATA MisMatch :: ------")
          `uvm_info(get_type_name(),$sformatf("Addr: %0h",mem_pkt.addr),UVM_LOW)
          `uvm_info(get_type_name(),$sformatf("Expected Data: %0h Actual Data: %0h",sc_mem[mem_pkt.addr],mem_pkt.rdata),UVM_LOW)
          `uvm_info(get_type_name(),"------------------------------------",UVM_LOW)
        end
      end
    end
  endtask : run_phase
  
endclass : uvm_template_scoreboard

`endif
