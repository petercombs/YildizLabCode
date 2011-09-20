WHTrackDefaults('Method', 'Gauss2DJILA', 'PixelSize', 106.667, 'PixelPadding', 15)
spotlists = dir('Red*_spotlist.txt');
for i = 1:length(spotlists)
    fn = spotlists(i).name
    WHTrackHighRes(fn)
    if isdir(fn(1:end-13))
        delete([fn(1:end-13), '/*'])
        rmdir(fn(1:end-13))
    end
    movefile('Traces', fn(1:end-13))
end
delete *xy_only.txt

%%
WHTrackDefaults('Method', 'Gauss2DJILA', 'PixelSize', 106.667, 'PixelPadding', 7)
spotlists = dir('Dyn*spotlist.txt');
for i = 1:length(spotlists)
    fn = spotlists(i).name
    WHTrackHighRes(fn)
    if isdir(fn(1:end-13))
        delete([fn(1:end-13), '/*'])
        rmdir(fn(1:end-13))
    end
    movefile('Traces', fn(1:end-13))
end

delete *xy_only.txt
