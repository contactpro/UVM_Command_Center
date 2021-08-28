// 
// Author: 
// Filename: uvm_template_top.sv  
// Version: Demo       
// Description: testbench top template for UVM Testbench Builder
// Language: SystemVerilog and UVM Libraries
//
`ifndef PKT_MEM_TB_TOP
`define PKT_MEM_TB_TOP

import uvm_pkg::*;
`include "C:/Users/HP/WORK_UVM/uvm-1.1d/src/uvm_macros.svh"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/uvm_templates/uvm_template_interface.sv"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/uvm_templates/uvm_template_base_test.sv"

module uvm_template_top;
  timeprecision  1ps;
  timeunit       1ns;
  
  //clock and reset signal declaration
  bit clk;
  bit reset;
  
  // environment class instance
  uvm_template_env env_inst_in_top;
  
  // interface instance
  my_if intf(clk,reset);
  
  // memory DUT instance
  uvm_template_memory_dut DUT (
    .clk(intf.clk),
    .reset(intf.reset),
    .addr(intf.addr),
    .wr_en(intf.wr_en),
    .rd_en(intf.rd_en),
    .wdata(intf.wdata),
    .rdata(intf.rdata)
   );  
  
  
  //clock generation
  always #5 clk = ~clk;
  
  //reset generation
  initial begin
    reset = 1;
    #30 reset = 0;
  end


  // enabling the wave dump
  initial begin 
    // uvm_config_db#(virtual my_if)::set(null,"uvm_test_top.env.agnt+","vif",intf);
    //enable wave dump
    $dumpfile("dump.vcd"); 
    $dumpvars;
  end
  
  // passing the interface handle to 
  // the lower heirarchy using set method   
  // calling test 
  initial begin 
  	`uvm_info("TOP","In TOP initial block . . .",UVM_MEDIUM)
  	env_inst_in_top = new("uvm_template_env"); // null);
    uvm_config_db#(virtual my_if)::set(null,"*","vif",intf); 	
    run_test("uvm_template_base_test");
  end
  
endmodule: uvm_template_top

`endif
