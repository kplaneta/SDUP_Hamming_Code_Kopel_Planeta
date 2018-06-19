`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 06.06.2018 13:35:21
// Design Name: 
// Module Name: ham_encode
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module ham_encode( clk, in, out, reset );
parameter n=15,k=11;
input clk; // ????
output [n-1:0] out;
input [k-1:0] in;
input reset;
reg [n-1:0] out;
integer i,j;

always @(posedge clk or posedge reset)
begin
    if(reset)
        out = 0;
    else
        begin
        i=0; j=0;
        while((i<n) || (j<k))
             begin
                while(i==0 || i==1 || i==3 || i==7)
                begin out[i] = 0;
                    i=i+1;
                end
            out[i] = in[j];
            i=i+1;
            j=j+1; 
            end
        if(^(out & 15'b101_0101_0101_0101))
          out[0] = ~out[0];
        if(^(out & 15'b110_0110_0110_0110))
           out[1] = ~out[1];
        if(^(out & 15'b111_1000_0111_1000))
           out[3] = ~out[3];
        if(^(out & 15'b111_1111_1000_0000))
           out[7] = ~out[7];
        end
end
endmodule