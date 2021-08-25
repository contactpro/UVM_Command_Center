// 
// Author: 
// Filename: uvm_template_memory_dut.sv  
// Version: Demo       
// Description: memory_dut template for UVM Testbench Builder
// Language: SystemVerilog and UVM Libraries
//
`ifndef PKT_MEM_DUT
`define PKT_MEM_DUT

import uvm_pkg::*;
`include "C:/Users/HP/WORK_UVM/uvm-1.1d/src/uvm_macros.svh"

module uvm_template_memory_dut
  #( parameter ADDR_WIDTH = 2,
     parameter DATA_WIDTH = 8 ) (
    input clk,
    input reset,
    
    //control signals
    input [ADDR_WIDTH-1:0]  addr,
    input                   wr_en,
    input                   rd_en,
    
    //data signals
    input  [DATA_WIDTH-1:0] wdata,
    output reg [DATA_WIDTH-1:0] rdata
  ); 
  
  //Memory
  reg [DATA_WIDTH-1:0] mem [2**ADDR_WIDTH];

  //Reset 
  always @(posedge reset) 
    for(int i=0;i<2**ADDR_WIDTH;i++) mem[i]=8'hFF;
   
  // Write data to Memory
  always @(posedge clk) 
    if (wr_en)    mem[addr] <= wdata;

  // Read data from memory
  always @(posedge clk)
    if (rd_en) rdata <= mem[addr];

endmodule

`endif