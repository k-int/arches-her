define([
    'jquery',
    'knockout',
], function($, ko) {
    // apply aria attributes to the element when an observable changes between true and false
    // e.g. <div data-bind="onReportSectionToggleAria: visible.names, sectionName: '{% trans "Section Name" %}'"></div>
    ko.bindingHandlers.onReportSectionToggleAria = {
        update: function(element, valueAccessor, allBindings) {
            var value = ko.utils.unwrapObservable(valueAccessor());
            var sectionName = allBindings.get('sectionName') || '';

            if (value) {
                $(element).attr('aria-expanded', 'true');
                $(element).attr('aria-label', sectionName + ' section expanded. Click to collapse section');
                $(element).addClass('fa-angle-double-right');
                $(element).removeClass('fa-angle-double-up');


            } else {
                $(element).attr('aria-expanded', 'false');
                $(element).attr('aria-label', sectionName + ' section collapsed. Click to expand section');
                $(element).removeClass('fa-angle-double-right');
                $(element).addClass('fa-angle-double-up');
            }
        }
    };


    return;
});
