    def sort(self):
        """
        Sort the robot's list.
        """
        # Selection Sort solution
        self.swap_item()
        self.set_light_on()

        while self.light_is_on():
            # move right and find the smallest item that has not been sorted
            while self.move_right():
                if self.compare_item() > 0:
                    self.swap_item()
            # if the robot is at the end of the list and all items are sorted, we're done
            if self.compare_item() is None and self.can_move_right() is False:
                # place the current item down in the list and turn light off to indicate the list is sorted
                self.swap_item()
                self.set_light_off()
                break
            else:
                # find the spot in the list that is holding None
                # place the item in that position
                # move right and swap
                while self.move_left():
                    if self.compare_item() is None:
                        self.swap_item()
                        self.move_right()
                        self.swap_item()
                        break
​
        # Bubble Sort solution

        # self.set_light_off()
        # while not self.light_is_on():
        #     self.set_light_on()
        #     while self.can_move_right():
        #         self.swap_item()
        #         self.move_right()
        #         if self.compare_item() > 0:
        #             self.swap_item()
        #             self.set_light_off()
        #         self.move_left()
        #         self.swap_item()
        #         self.move_right()
        #     if self.light_is_on():
        #         break
        #     self.set_light_on()
        #     while self.can_move_left():
        #         self.swap_item()
        #         self.move_left()
        #         if self.compare_item() < 0:
        #             self.swap_item()
        #             self.set_light_off()
        #         self.move_right()
        #         self.swap_item()
        #         self.move_left()