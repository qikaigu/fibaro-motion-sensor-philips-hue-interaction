--[[
%% properties
5 value
%% events
%% globals
--]]

local startSource = fibaro:getSourceTrigger();
local http = net.HTTPClient();
local url = 'http://192.168.0.14:5000/my_home/entrance_lights/0';  -- server entry point

if (
 ( tonumber(fibaro:getValue(5, "value")) == 0 )  -- get the motion sensor signal
or
startSource["type"] == "other"
)
then
  http:request(
    url,
    {
      options={
        method='GET'
      },
      success = function(resp)
        if resp.status == 200 then
          fibaro:debug(resp.status)
        else
          fibaro:debug(resp.status)
        end
      end
    }
  );
end
